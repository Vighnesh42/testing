from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Flight
from datetime import datetime

app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///flights.db"
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# City names dictionary
city_names = {
    'DEL': 'Delhi (DEL)',
    'BOM': 'Mumbai (BOM)',
    'BLR': 'Bengaluru (BLR)',
    'HYD': 'Hyderabad (HYD)',
    'MAA': 'Chennai (MAA)',
    'CCU': 'Kolkata (CCU)',
    'COK': 'Kochi (COK)',
    'AMD': 'Ahmedabad (AMD)',
    'PNQ': 'Pune (PNQ)',
    'GOI': 'Goa (GOI)',
    'IXC': 'Chandigarh (IXC)',
    'ATQ': 'Amritsar (ATQ)',
    'JAI': 'Jaipur (JAI)',
    'LUH': 'Ludhiana (LUH)',
    'PAT': 'Patna (PAT)',
    'LKO': 'Lucknow (LKO)',
    'VNS': 'Varanasi (VNS)',
    'BDQ': 'Vadodara (BDQ)',
    'RPR': 'Raipur (RPR)',
    'BBI': 'Bhubaneswar (BBI)',
    'TRV': 'Thiruvananthapuram (TRV)',
    'IXR': 'Ranchi (IXR)',
    'IXJ': 'Jammu (IXJ)',
    'IXA': 'Agartala (IXA)',
    'GAU': 'Guwahati (GAU)',
    'IXZ': 'Port Blair (IXZ)',
    'IXB': 'Bagdogra (IXB)',
    'VTZ': 'Visakhapatnam (VTZ)',
    'IMF': 'Imphal (IMF)',
    'SXR': 'Srinagar (SXR)',
    'IXL': 'Leh (IXL)',
    'IXW': 'Jamshedpur (IXW)',
    'CCJ': 'Kozhikode (CCJ)',
    'IXM': 'Madurai (IXM)',
    'IXE': 'Mangalore (IXE)',
    'IXD': 'Allahabad (IXD)',
    'IXH': 'Kailashahar (IXH)',
    'IXG': 'Belgaum (IXG)',
    'IXY': 'Kandla (IXY)',
    'HJR': 'Khajuraho (HJR)',
    'ISK': 'Nashik (ISK)',
    'TIR': 'Tirupati (TIR)',
    'IXK': 'Keshod (IXK)',
    'KUU': 'Bhuntar (Kullu) (KUU)',
    'STV': 'Surat (STV)',
    'IXP': 'Pathankot (IXP)',
    'SHL': 'Shillong (SHL)',
    'VGA': 'Vijayawada (VGA)',
    'TRZ': 'Tiruchirapalli (TRZ)',
    'IXU': 'Aurangabad (IXU)',
    'RJA': 'Rajahmundry (RJA)',
    'IXN': 'Khowai (IXN)',
    'PNY': 'Pondicherry (PNY)',
    'IXG': 'Belagavi (Belgaum) (IXG)',
    'JLR': 'Jabalpur (JLR)',
    'HBX': 'Hubli (HBX)',
    'TEZ': 'Tezpur (TEZ)',
    'MYQ': 'Mysuru (MYQ)',
    'VDY': 'Vidyanagar (VDY)',
    'NAG': 'Nagpur (NAG)',
    'IXS': 'Silchar (IXS)',
    'DED': 'Dehradun (DED)',
    'ZER': 'Zero (Ziro) (ZER)',
    'UDR': 'Udaipur (UDR)',
    'IDR': 'Indore (IDR)',
    'VTZ': 'Visakhapatnam (VTZ)',
}


@app.route('/', methods=['GET', 'POST'])
def index():
    origins = session.query(Flight.origin).distinct().all()
    destinations = session.query(Flight.destination).distinct().all()

    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        selected_date = request.form['departure_date']
      

        # Convert the selected date to a datetime object to extract the weekday
        datetime_selected_date = datetime.strptime(selected_date, "%Y-%m-%d")
        selected_weekday = datetime_selected_date.weekday()

        # Modify the query to include the weekday filter
        flights = session.query(Flight).filter(
            Flight.origin == origin,
            Flight.destination == destination,
            Flight.depart_weekday == selected_weekday
        ).all()

        return render_template(
            'index.html',
            flights=flights,
            origins=origins,
            destinations=destinations,
            selected_origin=origin,
            selected_destination=destination,
            selected_date=selected_date,
            city_names=city_names,
       
        )
    else:
        return render_template('index.html', origins=origins, destinations=destinations, city_names=city_names)

#ABOUT page ,,,,,,
@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

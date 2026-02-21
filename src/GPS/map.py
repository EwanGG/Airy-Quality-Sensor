import folium
import pandas as pd

def generate_map():

    data = pd.read_csv("../data/GPS/GPS.csv", name=["lat", "lon", "gas"])

    m = folium.Map(location=[data.lat.mean(), data.lon.mean()], zoom_start=5)

    for _, row in data.iterrows():
        color = "green" if row.gas > 100000 else "red"

        folium.CircleMarker(
            location=[row.lat, row.lon],
            radius=8,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"Gas: {row.gas}"
        ).add_to(m)

    m.save("air_quality_map.html")
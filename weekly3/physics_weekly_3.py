import folium as fo
import pandas as pd
import math

data = pd.read_excel("Location GPS 2025-02-01 17-38-11.xls")

latitudes = data['Latitude (°)']
longitudes = data['Longitude (°)']
trail_coordinates = []

m = fo.Map(location=[65.059533, 25.472295], zoom_start=15)
fo.Marker([65.059533, 25.472295], popup='Linnanmaa').add_to(m)

for i in range(len(latitudes)):
    trail_coordinates.append([latitudes[i], longitudes[i]])

fo.PolyLine(trail_coordinates, tooltip="Polku", color='red').add_to(m)

m.save('path.html')

print("Map saved to path.html")

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

total_distance = 0
for i in range(len(latitudes) - 1):
    total_distance += haversine(latitudes[i], longitudes[i], latitudes[i + 1], longitudes[i + 1])

print("Total distance: {:.2f} km".format(total_distance))



"""
ax[1].plot(time, acceleration_y, label='Y')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
ax[0].grid()
plt.legend()

ax[2].plot(time, acceleration_z, label='Z')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
ax[0].grid()
plt.legend()
"""

"""
ax[1].plot(time, y_filtered, label='Y')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
ax[1].grid()
plt.legend()

ax[2].plot(time, z_filtered, label='Z')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
ax[2].grid()
plt.legend()
"""

"""
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(time, acceleration_x, label='X')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
ax.grid()
st.pyplot(fig)
"""
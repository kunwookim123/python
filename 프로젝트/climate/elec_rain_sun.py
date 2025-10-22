import pandas as pd
import folium
import os

# ===== 파일 경로 =====
sun_path = r"C:\Users\UserK\Documents\일조_일사_통합평균_2020_2024.csv"
rain_path = r"C:\Users\UserK\Documents\강수량_통합평균_2020_2024.csv"
output_path = r"C:\Users\UserK\Documents\output\태양광_강수량_통합지도.html"

# ===== 데이터 불러오기 =====
sun_df = pd.read_csv(sun_path)
rain_df = pd.read_csv(rain_path)

sun_df.rename(columns={"통합지역": "지역"}, inplace=True)
rain_df.rename(columns={"통합지역": "지역"}, inplace=True)

# ===== 병합 =====
merged = pd.merge(sun_df, rain_df, on="지역", how="outer")

# ===== 북부 지역 병합 =====
replace_dict = {
    "북강릉": "강릉", "북부산": "부산",
    "북창원": "창원", "북춘천": "춘천",
    "서청주": "청주"
}
merged["지역"] = merged["지역"].replace(replace_dict)

# ===== 평균 재계산 =====
merged = merged.groupby("지역", as_index=False).mean(numeric_only=True)

# ===== 태양광 발전량 계산 =====
AREA = 10
EFFICIENCY = 0.20
PR = 0.75
MJ_to_kWh = 0.2778

merged["예상발전량(kWh/m²)"] = merged["합계 일사량(MJ/m2)"] * MJ_to_kWh * EFFICIENCY * PR
merged["예상총발전량(kWh)"] = merged["예상발전량(kWh/m²)"] * AREA

# ===== 전국 주요 좌표 =====
coords = {
    "서울": [37.5714, 126.9658], "인천": [37.4772, 126.6249], "수원": [37.2578, 127.0109],
    "강릉": [37.7519, 128.8761], "춘천": [37.9027, 127.7354], "청주": [36.6424, 127.4890],
    "대전": [36.3504, 127.3845], "전주": [35.8204, 127.1086], "광주": [35.1631, 126.8516],
    "대구": [35.8714, 128.6014], "부산": [35.1796, 129.0756], "울산": [35.5384, 129.3114],
    "창원": [35.2270, 128.6811], "제주": [33.4996, 126.5312], "서귀포": [33.2530, 126.5600],
    # 추가 좌표 필요 시 여기에 계속 확장 가능
}

# ===== 지도 생성 =====
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

solar_layer = folium.FeatureGroup(name="☀️ 예상 발전량")
rain_layer = folium.FeatureGroup(name="🌧️ 강수량")
combo_layer = folium.FeatureGroup(name="☀️🌧️ 발전↑ + 강수↓")

# ===== 평균 계산 =====
solar_mean = merged["예상총발전량(kWh)"].mean()
rain_mean = merged["평균강수량(mm)"].mean()

# ===== 지도에 점 표시 =====
for _, row in merged.iterrows():
    name = row["지역"]
    if name not in coords:
        continue

    lat, lon = coords[name]
    solar = row["예상총발전량(kWh)"]
    rain = row["평균강수량(mm)"]

    popup_html = f"""
    <div style="font-size:13px; text-align:center;">
        <b>{name}</b><br>
        ☀️ 예상 발전량: {solar:.1f} kWh<br>
        🌧️ 강수량: {rain:.1f} mm
    </div>
    """

    # ☀️ 태양광
    folium.CircleMarker(
        location=[lat, lon],
        radius=max(4, solar * 0.004),
        color="orange",
        fill=True,
        fill_color="orange",
        fill_opacity=0.6,
        popup=popup_html
    ).add_to(solar_layer)

    # 🌧️ 강수량
    folium.CircleMarker(
        location=[lat, lon],
        radius=max(4, rain * 0.01),
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.5,
        popup=popup_html
    ).add_to(rain_layer)

    # ☀️🌧️ 교집합
    if solar > solar_mean and rain < rain_mean:
        folium.CircleMarker(
            location=[lat, lon],
            radius=7,  # 기존보다 살짝 줄임
            color="green",
            fill=True,
            fill_color="green",
            fill_opacity=0.8,
            popup=f"{name}<br>☀️{solar:.1f} kWh<br>🌧️{rain:.1f} mm"
        ).add_to(combo_layer)

solar_layer.add_to(m)
rain_layer.add_to(m)
combo_layer.add_to(m)
folium.LayerControl(collapsed=False).add_to(m)

# 🔧 폴더 자동 생성 추가
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# ✅ 지도 저장
m.save(output_path)
print(f"✅ 지도 생성 완료: {output_path}")
m.save(output_path)
print(f"✅ 지도 생성 완료: {output_path}")
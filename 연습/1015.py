import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("data.csv")

# 하위 5% 백분위 기준값 계산
percentile_5 = df["값"].quantile(0.05)

# 하위 5%에 해당하는 지역 추출
bottom_5_percent = df[df["값"] < percentile_5]

# 결과 출력
print(f"하위 5% 기준값: {percentile_5:.2f}")
print("전국에서 하위 5%에 해당하는 지역:")
print(bottom_5_percent.to_string(index=False))




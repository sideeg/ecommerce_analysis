import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# إنشاء dataset وهمي
np.random.seed(42)
num_records = 1000

data = {
    'CustomerID': np.random.randint(1, 501, size=num_records),
    'SessionID': np.random.randint(1, 1001, size=num_records),
    'ProductID': np.random.randint(1, 1001, size=num_records),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Beauty'], size=num_records),
    'BrowsingDuration': np.random.randint(10, 300, size=num_records),  # بالثواني
    'AddedToCart': np.random.choice([0, 1], size=num_records),
    'Purchased': np.random.choice([0, 1], size=num_records),
    'PurchaseAmount': np.random.uniform(10, 500, size=num_records),
    'DiscountApplied': np.random.choice([0, 1], size=num_records),
    'TimeOfDay': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], size=num_records),
    'DayOfWeek': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], size=num_records),
    'DeviceType': np.random.choice(['Mobile', 'Desktop', 'Tablet'], size=num_records),
    'Source': np.random.choice(['Search', 'Ad', 'Direct'], size=num_records),
    'CustomerLocation': np.random.choice(['Urban', 'Suburban', 'Rural'], size=num_records),
    'CustomerAge': np.random.randint(18, 65, size=num_records),
    'CustomerGender': np.random.choice(['Male', 'Female'], size=num_records),
    'CustomerIncome': np.random.randint(30000, 100000, size=num_records),
    'CustomerType': np.random.choice(['New', 'Returning'], size=num_records),
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# معاينة بعض الصفوف من البيانات
print(df.head())


# تحليل العوامل التي تؤثر على معدل التحويل (Conversion Rate)
conversion_rate = df['Purchased'].mean() * 100
print(f'Conversion Rate: {conversion_rate:.2f}%')

# العوامل التي تؤثر على معدل التحويل
factor_analysis = df.groupby(['AddedToCart', 'DiscountApplied', 'DeviceType', 'Source', 'CustomerType'])['Purchased'].mean() * 100
print(factor_analysis)

# تحليل إحصائي لتوقعات المبيعات المستقبلية باستخدام متوسط قيمة الشراء
future_sales = df.groupby('DayOfWeek')['PurchaseAmount'].sum().sort_values(ascending=False)
print(f'Total sales by day of the week:\n{future_sales}')

# عرض النتائج باستخدام الرسوم البيانية
plt.figure(figsize=(10,6))
sns.barplot(x=future_sales.index, y=future_sales.values)
plt.title('Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Sales')
plt.show()

# تقديم توصيات لتحسين الأداء
print("Recommendations:")
if conversion_rate < 2.0:
    print("- Consider optimizing checkout flow to increase conversion.")
if df['DiscountApplied'].mean() > 0.5:
    print("- Discounts are highly used, consider revising discount strategies.")
if df['Source'].value_counts(normalize=True)['Ad'] > 0.4:
    print("- Ads are a significant traffic source, consider focusing on search optimizations.")
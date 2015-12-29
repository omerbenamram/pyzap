# pyzap

www.zap.co.il is Israel's biggest price comparison site!  
However, it has a terrible GUI..  

I've created pyzap :zap: to allow fast scraping for convinient price comparison

# How to use?
```python
import pyzap
pyzap.search(keyword, category=pyzap.ZapCategories.Electronics.TV)
```

if you're using the IPython Notebook, viewing of the results with pandas is recommended!
```python
import pyzap
import pandas as pd

results = pyzap.search('4k', category=pyzap.ZapCategories.Electronics.TV)
df = pd.DataFrame(results).transpose().fillna('')
df
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>max_price</th>
      <th>min_price</th>
      <th>גודל מסך</th>
      <th>טכנולוגיה</th>
      <th>טלוויזיה קעורה</th>
      <th>יצרן</th>
      <th>ממיר דיגיטלי</th>
      <th>רזולוציה</th>
      <th>תאריך כניסה לזאפ</th>
      <th>תדר תצוגה</th>
      <th>תלת מימד</th>
      <th>‏High Definition</th>
      <th>‏Smart TV</th>
      <th>‏WiFi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>טלויזיה Hisense LTDN42K3201UWAU LED  ‏42 ‏אינטש</th>
      <td>2570</td>
      <td>2570</td>
      <td>42‏ אינטש</td>
      <td>LED</td>
      <td></td>
      <td>Hisense</td>
      <td>DVB-T</td>
      <td>3840x2160</td>
      <td>10/2015</td>
      <td>Hz‏ 120</td>
      <td>ללא</td>
      <td>4K</td>
      <td>Smart TV</td>
      <td>כולל WiFi</td>
    </tr>
    <tr>
      <th>טלויזיה Skyworth 42E790 LED  ‏42 ‏אינטש</th>
      <td>3490</td>
      <td>3148</td>
      <td>42‏ אינטש</td>
      <td>LED</td>
      <td></td>
      <td>Skyworth</td>
      <td></td>
      <td>3840x2160</td>
      <td>11/2014</td>
      <td></td>
      <td>פסיבי</td>
      <td>4K</td>
      <td>Smart TV</td>
      <td>כולל WiFi</td>
    </tr>
    <tr>
      <th>טלויזיה Skyworth LED42E790 4K LED  ‏42 ‏אינטש</th>
      <td>3199</td>
      <td>3199</td>
      <td>42‏ אינטש</td>
      <td>LED</td>
      <td></td>
      <td>Skyworth</td>
      <td>DVB-T</td>
      <td>3840x2160</td>
      <td>2/2015</td>
      <td></td>
      <td>אקטיבי</td>
      <td>4K</td>
      <td>Smart TV</td>
      <td>כולל WiFi</td>
    </tr>
    <tr>
      <th>טלויזיה TCL LED40E5800US LED  ‏40 ‏אינטש</th>
      <td>3390</td>
      <td>3249</td>
      <td>40‏ אינטש</td>
      <td>LED</td>
      <td></td>
      <td>TCL</td>
      <td>DVB-T</td>
      <td>3840x2160</td>
      <td>6/2015</td>
      <td>Hz‏ 120</td>
      <td>ללא</td>
      <td>4K</td>
      <td>Smart TV</td>
      <td>ללא WiFi</td>
    </tr>
    <tr>
      <th>טלויזיה LG 40UB809Y LED  ‏40 ‏אינטש</th>
      <td>3545</td>
      <td>3545</td>
      <td>40‏ אינטש</td>
      <td>LED</td>
      <td></td>
      <td>LG</td>
      <td>DVB-T</td>
      <td>3840x2160</td>
      <td>4/2015</td>
      <td>Hz‏ 900</td>
      <td>ללא</td>
      <td>4K</td>
      <td>Smart TV</td>
      <td>כולל WiFi</td>
    </tr>
  </tbody>
</table>
....

or use from command line (still a little rough with unicode support for argv in Windows).  
(and get awesome excel support via pandas)

    pyzap --help
   

or just 

    pyzap
    
to get interactive prompt!

##Installation:
- clone the repo
- python src/setup.py

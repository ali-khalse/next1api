# Next1Api
---
## Installing Requests and Supported Versions
next1api officially supports Python 3.5+
<br>
next1api is available on PyPI:

```console
$ python -m pip install next1api
```
---
#
```python
from next1api import Music
#search
>>> C = Music()
>>> C.search("تست")

[{'name': 'دانلود ریمیکس دی جی فلیکس به نام دشتستانی', 'url': 'https://nex1music.ir/ریمیکس-دی-جی-فلیکس-دشتستانی/'}, {'name': 'دانلود آهنگ مرداد و تنیلر به نام رویا', 'url': 'https://nex1music.ir/آهنگ-مرداد-تنیلر-رویا/'}, {'name': 'دانلود آهنگ سامان دانشور به نام وقتی نیستی', 'url': 'https://nex1music.ir/آهنگ-سامان-دانشور-وقتی-نیستی/'}, {'name': 'دانلود آهنگ مهران و مرتضی به نام انرژی خاص', 'url': 'https://nex1music.ir/آهنگ-مهران-مرتضی-انرژی-خاص/'}, {'name': 'دانلود آهنگ مجید رومیانی و سهیل سکاکی به نام نگاهم کن', 'url': 'https://nex1music.ir/آهنگ-مجید-رومیانی-سهیل-سکاکی-نگاهم-کن/'}, {'name': 'دانلود آهنگ بهروز کیانی به نام دیوونه', 'url': 'https://nex1music.ir/آهنگ-بهروز-کیانی-دیوونه/'}, {'name': 'دانلود آهنگ آنهولی به نام اگه اینو بفهمی', 'url': 'https://nex1music.ir/آهنگ-آنهولی-اگه-اینو-بفهمی/'}, {'name': 'دانلود آهنگ حسن حیدرپور به نام لیلا', 'url': 'https://nex1music.ir/آهنگ-حسن-حیدرپور-لیلا/'}, {'name': 'دانلود آهنگ مستر چنج به نام میمونم', 'url': 'https://nex1music.ir/آهنگ-مستر-چنج-میمونم/'}, {'name': 'دانلود آهنگ بهزاد ملک زاده به نام پروونه ی قلبم', 'url': 'https://nex1music.ir/آهنگ-بهزاد-ملک-زاده-پروونه-ی-قلبم/'}, {'name': 'دانلود آهنگ مانی رعد به نام هدف', 'url': 'https://nex1music.ir/آهنگ-مانی-رعد-هدف/'}, {'name': 'دانلود آهنگ آریا نوید به نام بهار', 'url': 'https://nex1music.ir/آهنگ-آریا-نوید-بهار/'}, {'name': 'دانلود آهنگ دانیال داراب به نام چشمک', 'url': 'https://nex1music.ir/آهنگ-دانیال-داراب-چشمک/'}, {'name': 'دانلود آهنگ سعید داوری به نام فرشته', 'url': 'https://nex1music.ir/آهنگ-سعید-داوری-فرشته/'}, {'name': 'دانلود آهنگ پرویز بابایی به نام داره میره', 'url': 'https://nex1music.ir/آهنگ-پرویز-بابایی-داره-میره/'}, {'name': 'دانلود آهنگ مجتبی پورعلی به نام رگ خواب', 'url': 'https://nex1music.ir/آهنگ-مجتبی-پورعلی-رگ-خواب/'}, {'name': 'دانلود آهنگ رامین بیباک به نام سرزنش', 'url': 'https://nex1music.ir/آهنگ-رامین-بیباک-سرزنش/'}, {'name': 'دانلود آهنگ احسان دلبندی به نام دیوانگی', 'url': 'https://nex1music.ir/آهنگ-احسان-دلبندی-دیوانگی/'}, {'name': 'دانلود آهنگ حنان به نام مدام', 'url': 'https://nex1music.ir/آهنگ-حنان-مدام/'}, {'name': 'دانلود آهنگ مجید خراطها به نام یک ماه و چهل روز', 'url': 'https://nex1music.ir/آهنگ-مجید-خراطها-یک-ماه-چهل-روز/'}]

#download
>>> C.download("https://nex1music.ir/آهنگ-احسان-دلبندی-دیوانگی/")

{'music': [{'k': 'اصلی', 'u': 'https://dl.nex1music.ir/1399/08/16/Ehsan Delbandi - Divanegi.mp3'}, {'k': '128', 'u': 'https://dl.nex1music.ir/1399/08/16/Ehsan Delbandi - Divanegi [128].mp3'}, {'k': '64', 'u': 'https://dl.nex1music.ir/1399/08/16/Ehsan Delbandi - Divanegi [64].mp3'}], 'date': ' 16 آبان 1399 ', 'name': 'دانلود آهنگ احسان دلبندی به نام دیوانگی', 'M_name': 'احسان دلبندی دیوانگی', 'tumbnial': 'https://nex1music.ir/upload/2020-11-06/ehsan-delbandi-divanegi-2020-11-06-16-16-45.jpg'}
```
---



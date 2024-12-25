from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# ----------------------
# 1) Language Translations
# ----------------------
TRANSLATIONS = {
    'en': {
        'page_title': "SmokeX Calculator",
        'nav_brand': "SmokeX",
        'header_title': "Smoking Cost & Life Impact",
        'header_subtitle': "Calculate how much you spend, how much life you lose, and get a rough idea of your possible death age.",
        'label_age': "How Old Are You?",
        'label_packs_day': "Packs Per Day",
        'label_cost_pack': "Cost of One Pack",
        'label_currency': "Currency",
        'label_projection': "Projection (Years)",
        'label_invest': "If Invested: Annual Return (%)",
        'label_days': "days",
        'button_calculate': "Calculate",
        'result_life_lost': "Estimated Life Lost per Month",
        'result_death_age': "Predicted Death Age",
        'result_death_desc': "Based on an average life expectancy of {0} years, you might pass away around the age of {1}.",
        'monthly_cost': "Monthly Cost",
        'yearly_cost': "Yearly Cost",
        'total_cost': "Total Cost Over {0} Year(s)",
        'invested_instead': "If Invested Instead (~{0}%/year)",
        'recalculate': "Recalculate",
        'footer_text': "SmokeX © 2024 - A Better Way to See Your Smoking Costs",
        'label_faq': "FAQ",
        # Expanded FAQ
        'faq_page_title': "FAQ - Detailed Explanations",
        'faq_intro': "Below is a detailed explanation of how we calculate monthly life lost, costs, etc. Click on a question to expand the answer.",
        'faq_return': "Return to Calculator",
        'faq_q1': "1) How do we calculate the Monthly Estimated Life Lost?",
        'faq_a1': """We approximate that each cigarette can shorten life by about 11 minutes (around 220 minutes per pack).
Over a month, we multiply your daily packs by 30, then by 220 minutes, converting to days.
Thus, “Aylık Tahmini Ömür Kaybı” is a rough figure to illustrate potential health impact.""",
        'faq_q2': "2) How do we calculate costs and investments?",
        'faq_a2': """We calculate your monthly cost by multiplying daily packs × 30 × cost per pack.
The 'If Invested' scenario uses a simple monthly compound interest formula with your chosen annual return percentage.""",
        'faq_q3': "3) Why assume a 75-year life expectancy?",
        'faq_a3': """75 is a rough average used for demonstration. Real expectancy depends on many factors (genetics, lifestyle, healthcare). This is purely illustrative."""
    },
    'tr': {
        'page_title': "SmokeX Hesaplayıcı",
        'nav_brand': "SmokeX",
        'header_title': "Sigara Maliyeti ve Yaşam Etkisi",
        'header_subtitle': "Ne kadar harcadığınızı, ne kadar ömür kaybettiğinizi ve tahmini ölüm yaşınızı hesaplayın.",
        'label_age': "Kaç Yaşındasınız?",
        'label_packs_day': "Günlük Paket Sayısı",
        'label_cost_pack': "Bir Paketin Maliyeti",
        'label_currency': "Para Birimi",
        'label_projection': "Öngörü (Yıl)",
        'label_invest': "Eğer Yatırılsaydı: Yıllık Getiri (%)",
        'label_days': "gün",
        'button_calculate': "Hesapla",
        'result_life_lost': "Aylık Tahmini Ömür Kaybı",
        'result_death_age': "Tahmini Ölüm Yaşı",
        'result_death_desc': "Ortalama yaşam beklentisinin {0} yıl olduğu varsayılırsa, yaklaşık {1} yaşında hayatınızı kaybedebilirsiniz.",
        'monthly_cost': "Aylık Maliyet",
        'yearly_cost': "Yıllık Maliyet",
        'total_cost': "{0} Yıl İçindeki Toplam Maliyet",
        'invested_instead': "Yatırılsaydı (yıllık ~%{0})",
        'recalculate': "Yeniden Hesapla",
        'footer_text': "SmokeX © 2024 - Sigara Maliyetini Görmenin Daha İyi Yolu",
        'label_faq': "SSS",
        # Expanded FAQ
        'faq_page_title': "SSS - Detaylı Açıklamalar",
        'faq_intro': "Aşağıda aylık tahmini ömür kaybı, maliyet hesaplaması vb. konularda detaylı açıklamalar bulabilirsiniz. Bir sorunun üzerine tıklayarak cevabı görebilirsiniz.",
        'faq_return': "Hesaplayıcıya Geri Dön",
        'faq_q1': "1) Aylık Tahmini Ömür Kaybı Nasıl Hesaplanır?",
        'faq_a1': """Yaklaşık olarak bir sigaranın ömrü ortalama 11 dakika kısalttığı varsayılır (bir pakette ~220 dakika).
Bir ayda, günlük paket sayınız × 30 × 220 dakika, daha sonra dakikayı güne çeviriyoruz.
Böylece “Aylık Tahmini Ömür Kaybı” yaklaşık bir sağlık etkisi göstergesidir.""",
        'faq_q2': "2) Maliyet ve Yatırım Hesaplamaları Nasıl Yapılır?",
        'faq_a2': """Aylık maliyet, günlük paket × 30 × paket başı maliyet formülüyle bulunur.
“Eğer Yatırılsaydı” kısmında, belirlediğiniz yıllık faiz oranına göre basit bir aylık bileşik faiz formülü kullanılır.""",
        'faq_q3': "3) Neden 75 yıllık bir yaşam beklentisi varsayılıyor?",
        'faq_a3': """75, demonstre amaçlı kabaca bir ortalama olarak alınmıştır. Gerçek yaşam beklentisi birçok faktöre (genetik, yaşam koşulları, sağlık hizmetleri vb.) bağlıdır. Bu sadece örnek olması için kullanılır."""
    },
    'az': {
        'page_title': "SmokeX Kalkulyatoru",
        'nav_brand': "SmokeX",
        'header_title': "Siqaretin Dəyəri və Həyata Təsiri",
        'header_subtitle': "Nə qədər xərclədiyinizi, nə qədər ömür itirdiyinizi və təxmini ölüm yaşınızı hesablayın.",
        'label_age': "Neçə Yaşınız Var?",
        'label_packs_day': "Gündəlik Paket Sayı",
        'label_cost_pack': "Bir Paket Qiyməti",
        'label_currency': "Valyuta",
        'label_projection': "Proyeksiya (İl)",
        'label_invest': "Əgər İnvestə Edilsəydi: İllik Gəlir (%)",
        'label_days': "gün",
        'button_calculate': "Hesabla",
        'result_life_lost': "Aylıq Təxmini Ömür İtkisi",
        'result_death_age': "Təxmini Ölüm Yaşı",
        'result_death_desc': "Orta ömür uzunluğunun {0} il olduğunu fərz etsək, təxminən {1} yaşında dünyadan köçə bilərsiniz.",
        'monthly_cost': "Aylıq Xərc",
        'yearly_cost': "İllik Xərc",
        'total_cost': "{0} İldə Toplam Xərc",
        'invested_instead': "İnvestə Edilsəydi (illik təxminən %{0})",
        'recalculate': "Yenidən Hesabla",
        'footer_text': "SmokeX © 2024 - Siqaret xərclərini görmənin daha yaxşı yolu",
        'label_faq': "FAQ",
        # Expanded FAQ
        'faq_page_title': "FAQ - Ətraflı İzahlar",
        'faq_intro': "Aşağıda aylıq təxmini ömür itkisi, xərclər və digər mövzular haqqında ətraflı izah verilmişdir. Suala klikləyərək cavabı aça bilərsiniz.",
        'faq_return': "Kalkulyatora Qayıt",
        'faq_q1': "1) Aylıq Təxmini Ömür İtkisi Necə Hesablanır?",
        'faq_a1': """Bir siqaretin təxminən 11 dəqiqə ömrü qısaltdığı güman edilir (bir paket ~220 dəqiqə).
Bir ay üçün gündəlik paket sayı × 30 × 220 dəqiqə və daha sonra dəqiqədən günə çeviririk.
Beləliklə, “Aylıq Təxmini Ömür İtkisi” siqaretin sağlamlığa təsirini təxmini göstərir.""",
        'faq_q2': "2) Xərclər və İnvestisiya Necə Hesablanır?",
        'faq_a2': """Aylıq xərc gündəlik paket sayı × 30 × bir paketin qiyməti ilə tapılır.
“Əgər İnvestə Edilsəydi” hissəsində illik faiz göstəricisi əsasında sadə aylıq mürəkkəb faiz düsturu tətbiq olunur.""",
        'faq_q3': "3) Niyə 75 illik ömür uzunluğu götürülür?",
        'faq_a3': """75 sadəcə nümayiş məqsədilə təxmini ortalama kimi götürülür. Real ömür uzunluğu bir çox faktordan (genetika, həyat tərzi, tibbi xidmətlər və s.) asılıdır. Bu yalnız nümunə olaraq istifadə olunur."""
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1) Determine chosen language from query string
    user_lang = request.args.get('lang', 'en')
    if user_lang not in TRANSLATIONS:
        user_lang = 'en'
    t = TRANSLATIONS[user_lang]

    if request.method == 'POST':
        # Collect form data
        age = float(request.form.get('age', 0))
        packs_per_day = float(request.form.get('packs_per_day', 0))
        cost_per_pack = float(request.form.get('cost_per_pack', 0))
        selected_currency = request.form.get('currency', 'USD')
        years_projection = float(request.form.get('years_projection', 1))
        invest_rate = float(request.form.get('invest_rate', 5))

        # Calculate monthly & yearly cost
        monthly_packs = packs_per_day * 30
        monthly_cost = monthly_packs * cost_per_pack
        yearly_cost = monthly_cost * 12
        total_cost_projection = yearly_cost * years_projection

        # If Invested Instead (simple compound interest)
        monthly_interest_rate = invest_rate / 100 / 12
        total_months = int(12 * years_projection)
        future_value = 0
        for _ in range(total_months):
            future_value += monthly_cost
            future_value *= (1 + monthly_interest_rate)
        future_value = round(future_value, 2)

        # Life lost calculation (rough)
        days_lost_monthly = round((packs_per_day * 30 * 0.15), 2)

        # Predicted death age
        average_life_expectancy = 75.0
        years_left_if_no_smoke = average_life_expectancy - age
        months_left = int(years_left_if_no_smoke * 12)
        total_days_lost = days_lost_monthly * months_left
        years_lost = total_days_lost / 365.0
        predicted_death_age = round(average_life_expectancy - years_lost, 1)

        return render_template(
            'index.html',
            lang=user_lang,
            t=t,
            show_results=True,
            days_lost_monthly=days_lost_monthly,
            selected_currency=selected_currency,
            monthly_cost=round(monthly_cost, 2),
            yearly_cost=round(yearly_cost, 2),
            total_cost_projection=round(total_cost_projection, 2),
            future_value=future_value,
            average_life_expectancy=int(average_life_expectancy),
            predicted_death_age=predicted_death_age,
            years_projection=int(years_projection),
            invest_rate=invest_rate
        )
    else:
        # GET request
        return render_template(
            'index.html',
            lang=user_lang,
            t=t,
            show_results=False
        )

# 2) FAQ ROUTE
@app.route('/faq')
def faq():
    user_lang = request.args.get('lang', 'en')
    if user_lang not in TRANSLATIONS:
        user_lang = 'en'
    t = TRANSLATIONS[user_lang]

    return render_template(
        'faq.html',
        lang=user_lang,
        t=t
    )


if __name__ == '__main__':
    app.run(debug=True)

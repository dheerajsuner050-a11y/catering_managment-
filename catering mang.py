# ==========================================
# CATERING MANAGEMENT CALCULATOR
# ALOO SABJI - BASE CALCULATION
# Base: 1000 People
# ==========================================

BASE_PEOPLE = 1000

# All quantities converted to grams
ingredients = {
    "प्याज": 7000,
    "लहसुन": 2000,
    "अदरक": 1000,
    "हरी मिर्च": 1500,
    "शिमला मिर्च": 3000,
    "हरा धनिया": 2000,
    "हरा मटर (छीलवा कर देना)": 10000,
    "बड़े आलू": 40000,
    "टमाटर देशी": 8000,

    "गरम मसाला": 250,
    "चाट मसाला": 200,
    "चना मसाला": 200,
    "किचन किंग मसाला": 200,
    "जीरा": 250,
    "लाल मिर्च": 2000,
    "हल्दी": 250,
    "धनिया पिसा": 500,
    "खड़ी लाल मिर्च": 100,
    "खड़ा धनिया": 500,
    "तेज पान": 100,
    "मूंगफली दाना": 3000,
    "तिल सफेद": 2000,
    "रिफाइंड तेल": 7000,
    "कस्तूरी मेथी": 100,
    "कश्मीरी मिर्च": 200,
    "खोपरा बूरा": 1000,
    "खसखस": 200,
    "कुकिंग ऑयल": 7000
}


def format_quantity(grams):
    """
    Convert grams into kg/grams for easy reading.
    """

    if grams >= 1000:
        kg = grams / 1000

        # If exact kg
        if kg.is_integer():
            return f"{int(kg)} kg"

        return f"{kg:.2f} kg"

    return f"{grams:.0f} gram"


def calculate_catering(number_of_people):

    multiplier = number_of_people / BASE_PEOPLE

    print("\n" + "=" * 55)
    print("        CATERING MANAGEMENT CALCULATOR")
    print("=" * 55)

    print(f"Base Calculation : {BASE_PEOPLE} People")
    print(f"Required People  : {number_of_people}")
    print("-" * 55)

    print(f"{'क्रमांक':<8}{'सामान':<30}{'मात्रा'}")
    print("-" * 55)

    for index, (item, base_quantity) in enumerate(
        ingredients.items(), start=1
    ):

        required_quantity = base_quantity * multiplier

        print(
            f"{index:<8}"
            f"{item:<30}"
            f"{format_quantity(required_quantity)}"
        )

    print("=" * 55)


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    try:
        people = int(input("\nकितने लोगों के लिए खाना बनाना है? "))

        if people <= 0:
            print("कृपया 0 से अधिक लोगों की संख्या डालें.")
            continue

        calculate_catering(people)

        again = input("\nक्या दूसरी संख्या के लिए calculation करें? (y/n): ")

        if again.lower() != "y":
            print("\nCalculator बंद किया गया.")
            break

    except ValueError:
        print("कृपया केवल संख्या डालें.")
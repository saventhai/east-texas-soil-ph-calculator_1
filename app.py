
import streamlit as st

# rest of your complete app.py code...
# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="East Texas Soil Amendment Calculator",
    page_icon="🌱",
    layout="centered"
)


# ============================================================
# 2. TITLE AND INTRODUCTION
# ============================================================

st.title("🌱 East Texas Soil Amendment Calculator")

st.write(
    """
    This tool helps farmers, land managers, and agricultural professionals
    compare measured soil pH with the optimal pH range of a selected crop.

    When soil pH is below the crop's recommended range, the calculator can
    estimate agricultural lime requirements using either:

    - a laboratory lime recommendation, or
    - a laboratory-measured Lime Buffer Capacity (LBC).
    """
)

st.info(
    "For the most reliable recommendation, use results from a recent "
    "laboratory soil test. Soil pH alone cannot determine an exact lime rate."
)


# ============================================================
# 3. CROP pH DATABASE
# ============================================================

crop_data = {
    "Almonds": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Muhammad et al., 2017"},
    "Apples": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Asparagus": {"min_ph": 6.0, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Avocados": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Barley": {"min_ph": 5.5, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Blueberries": {"min_ph": 4.5, "max_ph": 5.5, "reference": "UCONN, 2025"},
    "Broccoli": {"min_ph": 6.0, "max_ph": 7.0, "reference": "UCONN, 2025"},
    "Buckwheat": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Cabbage": {"min_ph": 5.8, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Caneberries": {"min_ph": 5.5, "max_ph": 6.5, "reference": "Strik & Bryla, 2015"},
    "Canola": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Ballagh et al., 2024"},
    "Cantaloupes": {"min_ph": 6.0, "max_ph": 6.8, "reference": "Boyhan et al., 2009"},
    "Carrots": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Cauliflower": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Celery": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Cherries": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Chick Peas": {"min_ph": 6.0, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Citrus": {"min_ph": 5.5, "max_ph": 6.5, "reference": "Morgan, 2019"},
    "Corn": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Cotton": {"min_ph": 5.8, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Cranberries": {"min_ph": 4.5, "max_ph": 5.5, "reference": "Havlin et al., 2016"},
    "Cucumbers": {"min_ph": 5.5, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Dry Beans": {"min_ph": 5.8, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Durum Wheat": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Flaxseed": {"min_ph": 5.5, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Garlic": {"min_ph": 6.0, "max_ph": 8.0, "reference": "Havlin et al., 2016"},
    "Grapes": {"min_ph": 5.5, "max_ph": 6.5, "reference": "UCONN, 2025"},
    "Honeydew Melons": {"min_ph": 6.0, "max_ph": 6.8, "reference": "Duncan & Ewing, 2015"},
    "Lentils": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Pavek & McGee, 2016"},
    "Lettuce": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Millet": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Sheahan, 2014"},
    "Mint": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Mustard": {"min_ph": 6.0, "max_ph": 7.5, "reference": "UCONN, 2025"},
    "Oats": {"min_ph": 5.5, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Olives": {"min_ph": 6.5, "max_ph": 8.0, "reference": "Bartolucci & Dhakal, 1999"},
    "Onions": {"min_ph": 6.0, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Oranges": {"min_ph": 5.8, "max_ph": 6.5, "reference": "Havlin et al., 2016"},
    "Peaches": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Peanuts": {"min_ph": 5.8, "max_ph": 6.5, "reference": "Havlin et al., 2016"},
    "Pears": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Peas": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Peppers": {"min_ph": 5.5, "max_ph": 6.5, "reference": "FAO, 2006"},
    "Plums": {"min_ph": 6.0, "max_ph": 7.5, "reference": "UCONN, 2025"},
    "Pomegranates": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Pop or Orn Corn": {"min_ph": 5.8, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Potatoes": {"min_ph": 4.8, "max_ph": 6.5, "reference": "UCONN, 2025"},
    "Prunes": {"min_ph": 6.0, "max_ph": 7.5, "reference": "UCONN, 2025"},
    "Pumpkins": {"min_ph": 5.5, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Radishes": {"min_ph": 5.8, "max_ph": 6.8, "reference": "Havlin et al., 2016"},
    "Rice": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Rostini et al., 2020"},
    "Rye": {"min_ph": 5.5, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Sorghum": {"min_ph": 6.0, "max_ph": 7.5, "reference": "FAO, 2006"},
    "Soybeans": {"min_ph": 5.5, "max_ph": 7.0, "reference": "FAO, 2006"},
    "Spring Wheat": {"min_ph": 6.0, "max_ph": 7.5, "reference": "FAO, 2006"},
    "Squash": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Strawberries": {"min_ph": 5.5, "max_ph": 6.5, "reference": "FAO, 2006"},
    "Sugarbeets": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Samuel & Dines, 2023"},
    "Sugarcane": {"min_ph": 5.5, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Sunflower": {"min_ph": 6.0, "max_ph": 7.0, "reference": "Havlin et al., 2016"},
    "Sweet Corn": {"min_ph": 5.5, "max_ph": 7.5, "reference": "Liu & Hanlon, 2012"},
    "Sweet Potatoes": {"min_ph": 5.5, "max_ph": 6.5, "reference": "UCONN, 2025"},
    "Tobacco": {"min_ph": 5.5, "max_ph": 6.0, "reference": "FAO, 2006"},
    "Tomatoes": {"min_ph": 5.5, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Turnips": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Walnuts": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"},
    "Watermelons": {"min_ph": 5.5, "max_ph": 6.5, "reference": "Liu & Hanlon, 2012"},
    "Winter Wheat": {"min_ph": 6.0, "max_ph": 7.5, "reference": "Havlin et al., 2016"}
}


# ============================================================
# 4. SOIL AND CROP INFORMATION
# ============================================================

st.header("1. Soil and Crop Information")

crop = st.selectbox(
    "Select your crop",
    options=list(crop_data.keys())
)

current_ph = st.number_input(
    "Measured soil pH",
    min_value=3.0,
    max_value=9.0,
    value=5.5,
    step=0.1,
    format="%.1f",
    help="Enter the soil pH from your soil-test result."
)

acreage = st.number_input(
    "Field size (acres)",
    min_value=0.1,
    max_value=100000.0,
    value=10.0,
    step=1.0,
    format="%.1f"
)


# ============================================================
# 5. GET CROP INFORMATION
# ============================================================

min_ph = crop_data[crop]["min_ph"]
max_ph = crop_data[crop]["max_ph"]
reference = crop_data[crop]["reference"]


# ============================================================
# 6. CROP pH ASSESSMENT
# ============================================================

st.header("2. Crop Soil pH Assessment")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Soil pH",
        f"{current_ph:.1f}"
    )

with col2:
    st.metric(
        "Minimum Optimal pH",
        f"{min_ph:.1f}"
    )

with col3:
    st.metric(
        "Maximum Optimal pH",
        f"{max_ph:.1f}"
    )

st.write(
    f"Recommended soil pH range for **{crop}**: "
    f"**{min_ph:.1f}–{max_ph:.1f}**"
)

st.caption(
    f"Crop pH reference: {reference}"
)


# ============================================================
# 7. DETERMINE SOIL pH STATUS
# ============================================================

if current_ph < min_ph:

    ph_difference = min_ph - current_ph

    st.warning(
        f"The measured soil pH is {ph_difference:.1f} pH units below "
        f"the lower end of the recommended range for {crop}. "
        "Agricultural lime may be needed."
    )

    lime_needed = True
    ph_status = "Below recommended range"

elif min_ph <= current_ph <= max_ph:

    st.success(
        f"The measured soil pH ({current_ph:.1f}) is within the "
        f"recommended range for {crop} "
        f"({min_ph:.1f}–{max_ph:.1f})."
    )

    lime_needed = False
    ph_status = "Within recommended range"

else:

    st.warning(
        f"The measured soil pH ({current_ph:.1f}) is above the "
        f"recommended range for {crop} "
        f"({min_ph:.1f}–{max_ph:.1f})."
    )

    st.info(
        "Do not apply agricultural lime based on this pH result because "
        "lime would increase soil pH further."
    )

    lime_needed = False
    ph_status = "Above recommended range"

st.write(
    f"**Soil pH status:** {ph_status}"
)


# ============================================================
# 8. LIME REQUIREMENT
# ============================================================

if lime_needed:

    st.header("3. Lime Requirement")

    st.info(
        "Soil pH indicates whether acidity may be a problem, but pH alone "
        "does not determine how many tons of lime are required. "
        "Choose the calculation method that matches your soil-test information."
    )

    lime_method = st.radio(
        "Choose calculation method",
        [
            "A. Laboratory lime recommendation",
            "B. Laboratory Lime Buffer Capacity (LBC)"
        ]
    )


    # ========================================================
    # METHOD A: LABORATORY RECOMMENDATION
    # ========================================================

    if lime_method == "A. Laboratory lime recommendation":

        st.success(
            "Preferred method: enter the lime recommendation provided "
            "by your soil-testing laboratory."
        )

        lab_lime_rate = st.number_input(
            "Laboratory lime recommendation (tons/acre)",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            help=(
                "Enter the lime recommendation reported by the soil-testing "
                "laboratory before adjustment for the quality of your lime product."
            )
        )

        ecce = st.number_input(
            "Lime product ECCE (%)",
            min_value=1.0,
            max_value=100.0,
            value=90.0,
            step=1.0,
            format="%.0f",
            key="ecce_lab",
            help=(
                "Enter the Effective Calcium Carbonate Equivalent (ECCE) "
                "from the lime product label, analysis certificate, "
                "or supplier information."
            )
        )

        if st.button(
            "Calculate Lime Requirement",
            type="primary",
            key="calculate_lab"
        ):

            adjusted_lime_rate = (
                lab_lime_rate /
                (ecce / 100.0)
            )

            total_lime = (
                adjusted_lime_rate *
                acreage
            )

            st.subheader("🌱 Lime Recommendation")

            result1, result2 = st.columns(2)

            with result1:

                st.metric(
                    "Application Rate",
                    f"{adjusted_lime_rate:.2f} tons/acre"
                )

            with result2:

                st.metric(
                    "Total Lime Required",
                    f"{total_lime:.1f} tons"
                )

            st.subheader("Calculation Summary")

            st.write(
                f"""
                **Crop:** {crop}

                **Current soil pH:** {current_ph:.1f}

                **Recommended crop pH range:** {min_ph:.1f}–{max_ph:.1f}

                **Laboratory lime recommendation:** {lab_lime_rate:.2f} tons/acre

                **Lime product ECCE:** {ecce:.0f}%

                **Field size:** {acreage:.1f} acres
                """
            )

            st.subheader(
                "How was the lime rate calculated?"
            )

            st.latex(
                r"\mathrm{Adjusted\ Lime\ Rate} = "
                r"\frac{\mathrm{Laboratory\ Lime\ Recommendation}}"
                r"{\mathrm{ECCE}/100}"
            )

            st.write(
                f"**{lab_lime_rate:.2f} ÷ ({ecce:.0f}/100) "
                f"= {adjusted_lime_rate:.2f} tons/acre**"
            )

            st.latex(
                r"\mathrm{Total\ Lime} = "
                r"\mathrm{Adjusted\ Lime\ Rate} "
                r"\times \mathrm{Field\ Area}"
            )

            st.write(
                f"**{adjusted_lime_rate:.2f} × {acreage:.1f} "
                f"= {total_lime:.1f} tons**"
            )

            st.success(
                f"Based on the laboratory recommendation and a lime product "
                f"with {ecce:.0f}% ECCE, approximately "
                f"{adjusted_lime_rate:.2f} tons/acre would be required. "
                f"For {acreage:.1f} acres, this is approximately "
                f"{total_lime:.1f} tons of lime material."
            )


    # ========================================================
    # METHOD B: LIME BUFFER CAPACITY
    # ========================================================

    else:

        st.warning(
            "Use this method only when your soil laboratory provides a "
            "Lime Buffer Capacity (LBC) expressed as mg CaCO₃ per kg soil "
            "per unit change in pH. Do not estimate LBC from soil pH alone."
        )

        target_ph = st.number_input(
            "Target soil pH",
            min_value=float(current_ph),
            max_value=float(max_ph),
            value=float(min_ph),
            step=0.1,
            format="%.1f",
            help=(
                "The lower end of the selected crop's recommended range "
                "is used as the default target."
            )
        )

        lbc = st.number_input(
            "Lime Buffer Capacity (mg CaCO₃/kg soil/pH unit)",
            min_value=1.0,
            max_value=5000.0,
            value=1000.0,
            step=50.0,
            format="%.0f",
            help=(
                "Enter the laboratory-measured LBC. Make sure your laboratory "
                "reports LBC in mg CaCO₃ per kg soil per pH unit."
            )
        )

        depth_in = st.number_input(
            "Soil depth to be amended (inches)",
            min_value=1.0,
            max_value=24.0,
            value=6.0,
            step=1.0,
            format="%.1f"
        )

        bulk_density = st.number_input(
            "Soil bulk density (g/cm³)",
            min_value=0.50,
            max_value=2.00,
            value=1.30,
            step=0.05,
            format="%.2f",
            help=(
                "Use a measured bulk density when available. "
                "The default 1.30 g/cm³ is only an example value."
            )
        )

        ecce_lbc = st.number_input(
            "Lime product ECCE (%)",
            min_value=1.0,
            max_value=100.0,
            value=90.0,
            step=1.0,
            format="%.0f",
            key="ecce_lbc",
            help=(
                "Enter the ECCE from the agricultural lime product label "
                "or supplier analysis."
            )
        )

        if st.button(
            "Estimate Lime Requirement",
            type="primary",
            key="calculate_lbc"
        ):

            # Required pH increase
            ph_change = (
                target_ph -
                current_ph
            )

            # Convert inches to meters
            depth_m = (
                depth_in *
                0.0254
            )

            # Convert g/cm3 to kg/m3
            bulk_density_kg_m3 = (
                bulk_density *
                1000.0
            )

            # Area of one acre in square meters
            acre_m2 = 4046.8564224

            # Soil mass per acre
            soil_mass_kg_acre = (
                acre_m2 *
                depth_m *
                bulk_density_kg_m3
            )

            # Required CaCO3 concentration
            caco3_mg_per_kg = (
                lbc *
                ph_change
            )

            # Total CaCO3 mass per acre
            caco3_kg_acre = (
                caco3_mg_per_kg *
                soil_mass_kg_acre /
                1_000_000.0
            )

            # Convert kg to US tons
            pure_caco3_tons_acre = (
                caco3_kg_acre /
                907.18474
            )

            # Correct for lime product ECCE
            adjusted_lime_rate = (
                pure_caco3_tons_acre /
                (ecce_lbc / 100.0)
            )

            # Total material for whole field
            total_lime = (
                adjusted_lime_rate *
                acreage
            )

            st.subheader(
                "🌱 Estimated Lime Requirement"
            )

            result1, result2 = st.columns(2)

            with result1:

                st.metric(
                    "Estimated Application Rate",
                    f"{adjusted_lime_rate:.2f} tons/acre"
                )

            with result2:

                st.metric(
                    "Estimated Total Lime",
                    f"{total_lime:.1f} tons"
                )

            st.subheader(
                "Calculation Summary"
            )

            st.write(
                f"""
                **Crop:** {crop}

                **Current soil pH:** {current_ph:.1f}

                **Target soil pH:** {target_ph:.1f}

                **Required pH increase:** {ph_change:.1f}

                **LBC:** {lbc:.0f} mg CaCO₃/kg soil/pH unit

                **Soil depth:** {depth_in:.1f} inches

                **Bulk density:** {bulk_density:.2f} g/cm³

                **Lime ECCE:** {ecce_lbc:.0f}%

                **Field size:** {acreage:.1f} acres
                """
            )

            st.subheader(
                "How was the estimate calculated?"
            )

            st.latex(
                r"\Delta pH = "
                r"pH_{\mathrm{target}} - "
                r"pH_{\mathrm{current}}"
            )

            st.write(
                f"**{target_ph:.1f} − {current_ph:.1f} "
                f"= {ph_change:.1f} pH units**"
            )

            st.latex(
                r"\mathrm{CaCO_3\ concentration} = "
                r"LBC \times \Delta pH"
            )

            st.write(
                f"**{lbc:.0f} × {ph_change:.1f} "
                f"= {caco3_mg_per_kg:.0f} mg CaCO₃/kg soil**"
            )

            st.latex(
                r"\mathrm{Soil\ Mass} = "
                r"\mathrm{Area} \times "
                r"\mathrm{Depth} \times "
                r"\mathrm{Bulk\ Density}"
            )

            st.write(
                f"Estimated soil mass represented by one acre: "
                f"**{soil_mass_kg_acre:,.0f} kg soil/acre**"
            )

            st.write(
                f"Pure CaCO₃ requirement: "
                f"**{pure_caco3_tons_acre:.2f} tons CaCO₃/acre**"
            )

            st.latex(
                r"\mathrm{Actual\ Lime\ Rate} = "
                r"\frac{\mathrm{Pure\ CaCO_3\ Requirement}}"
                r"{\mathrm{ECCE}/100}"
            )

            st.write(
                f"**{pure_caco3_tons_acre:.2f} ÷ "
                f"({ecce_lbc:.0f}/100) "
                f"= {adjusted_lime_rate:.2f} tons/acre**"
            )

            st.success(
                f"Using the entered LBC, soil depth, bulk density, and "
                f"{ecce_lbc:.0f}% ECCE lime, the estimated application rate "
                f"is {adjusted_lime_rate:.2f} tons/acre. "
                f"For {acreage:.1f} acres, approximately "
                f"{total_lime:.1f} tons of lime material would be required."
            )

            st.warning(
                "This result is an estimate based on the entered laboratory "
                "LBC and soil properties. Confirm the final lime application "
                "rate with a soil-testing laboratory or local Extension "
                "recommendation before field application."
            )


# ============================================================
# 9. pH WITHIN RECOMMENDED RANGE
# ============================================================

if min_ph <= current_ph <= max_ph:

    st.header(
        "3. Amendment Recommendation"
    )

    st.success(
        f"No lime application is indicated based on soil pH because "
        f"the measured pH of {current_ph:.1f} is within the recommended "
        f"range for {crop}."
    )

    st.info(
        "Continue routine soil testing because soil pH can change over "
        "time due to fertilizer use, rainfall, crop removal, "
        "and soil management."
    )


# ============================================================
# 10. pH ABOVE RECOMMENDED RANGE
# ============================================================

if current_ph > max_ph:

    st.header(
        "3. Amendment Recommendation"
    )

    st.warning(
        "Agricultural lime is not recommended because the measured soil "
        "pH is already above the selected crop's recommended range."
    )

    st.info(
        "A high soil pH does not automatically mean gypsum should be applied. "
        "Additional soil-test information is needed to determine whether "
        "sodicity or another soil chemical problem is present."
    )


# ============================================================
# 11. GYPSUM INFORMATION
# ============================================================

st.divider()

st.header(
    "🪨 Gypsum Assessment"
)

st.write(
    """
    Agricultural lime and gypsum serve different purposes.

    **Agricultural lime**
    neutralizes soil acidity and increases soil pH.

    **Agricultural gypsum**
    supplies calcium and sulfur but normally has little direct effect
    on soil pH. Gypsum should therefore not be recommended from soil
    pH alone.
    """
)

with st.expander(
    "What information would be needed for a gypsum recommendation?"
):

    st.write(
        """
        Depending on the purpose of the application, additional
        measurements may include:

        - Exchangeable Sodium Percentage (ESP)
        - Sodium Adsorption Ratio (SAR)
        - Cation Exchange Capacity (CEC)
        - Exchangeable sodium
        - Exchangeable calcium
        - Target ESP
        - Soil depth
        - Bulk density
        - Gypsum purity
        - Irrigation-water chemistry
        - Drainage and leaching conditions
        """
    )


# ============================================================
# 12. IMPORTANT INFORMATION
# ============================================================

st.divider()

st.header(
    "Important Information"
)

st.warning(
    """
    Soil pH alone cannot determine an exact agricultural lime requirement.
    Soils having the same pH may require very different quantities of lime
    because their buffering capacities differ.
    """
)

st.caption(
    """
    This application is intended as an educational and Extension
    decision-support tool. Crop pH ranges are based on the cited references.
    Final agricultural lime or gypsum applications should be based on
    representative soil sampling, appropriate laboratory analyses,
    crop requirements, lime-product quality, and local Extension or
    soil-testing laboratory recommendations.
    """
)

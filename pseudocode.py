#basic layout for the program
START PROGRAM

DISPLAY "Interview Outfit Helper"

# 1) Define choices
SET job_types = ["Tech", "Office/Corporate", "Retail/Customer-facing", "Trades/Hands-on", "Creative"]
SET interview_types = ["In-person", "Video", "Phone"]
SET budget_levels = ["0", "Under $50", "$50-$150", "$150+"]

# 2) Get job type
DISPLAY "Choose a job type:"
DISPLAY job_types as numbered list (1..5)
INPUT job_choice_number
WHILE job_choice_number is not between 1 and 5
    DISPLAY "Invalid choice. Please enter a number 1-5."
    INPUT job_choice_number
END WHILE
SET job_type = job_types[job_choice_number - 1]

# 3) Get interview type
DISPLAY "Choose interview type:"
DISPLAY interview_types as numbered list (1..3)
INPUT interview_choice_number
WHILE interview_choice_number is not between 1 and 3
    DISPLAY "Invalid choice. Please enter a number 1-3."
    INPUT interview_choice_number
END WHILE
SET interview_type = interview_types[interview_choice_number - 1]

# 4) Get budget
DISPLAY "Choose your budget:"
DISPLAY budget_levels as numbered list (1..4)
INPUT budget_choice_number
WHILE budget_choice_number is not between 1 and 4
    DISPLAY "Invalid choice. Please enter a number 1-4."
    INPUT budget_choice_number
END WHILE
SET budget_level = budget_levels[budget_choice_number - 1]

# 5) Determine recommendation (rules)
SET outfit_category = ""
SET top = ""
SET bottom = ""
SET shoes = ""
SET notes = ""
SET budget_tip = ""

IF job_type == "Office/Corporate" THEN
    outfit_category = "Business Professional"
    top = "Button-up shirt or blouse (solid color)"
    bottom = "Dress slacks or knee-length skirt"
    shoes = "Closed-toe dress shoes"
    notes = "Avoid loud patterns; keep accessories simple."
ELSE IF job_type == "Tech" THEN
    outfit_category = "Business Casual"
    top = "Polo, sweater, or simple blouse"
    bottom = "Chinos or dark jeans (no rips)"
    shoes = "Clean sneakers or casual dress shoes"
    notes = "Neat and comfortable; avoid graphic tees."
ELSE IF job_type == "Retail/Customer-facing" THEN
    outfit_category = "Clean Casual"
    top = "Solid shirt or blouse"
    bottom = "Clean jeans or slacks"
    shoes = "Closed-toe shoes"
    notes = "Prioritize a clean, friendly look."
ELSE IF job_type == "Trades/Hands-on" THEN
    outfit_category = "Practical Neat"
    top = "Clean collared shirt or plain long-sleeve"
    bottom = "Work pants or clean jeans"
    shoes = "Work boots or sturdy closed-toe shoes"
    notes = "Professional but practical; avoid overly formal wear."
ELSE IF job_type == "Creative" THEN
    outfit_category = "Smart Casual"
    top = "Layered top (jacket/cardigan) with solid shirt"
    bottom = "Slacks or dark jeans"
    shoes = "Clean shoes (casual or dressy)"
    notes = "Show personality, but keep it polished."
END IF

# 6) Adjust for interview type
IF interview_type == "Video" THEN
    notes = notes + " For video: prioritize a solid-color top, good lighting, and avoid stripes."
ELSE IF interview_type == "Phone" THEN
    notes = notes + " For phone: dress neat anyway—confidence matters."
END IF

# 7) Budget guidance
IF budget_level == "0" THEN
    budget_tip = "Use what you have: choose the cleanest, best-fitting items; iron if possible."
ELSE IF budget_level == "Under $50" THEN
    budget_tip = "Focus on one key item (top OR shoes). Consider thrift stores or discount retailers."
ELSE IF budget_level == "$50-$150" THEN
    budget_tip = "You can build a basic outfit: top + bottom, or add a simple blazer."
ELSE IF budget_level == "$150+" THEN
    budget_tip = "Consider investing in durable staples (shoes, blazer, slacks) you can reuse."
END IF

# 8) Display results
DISPLAY "--------------------------------"
DISPLAY "Recommendation:"
DISPLAY "Category: " + outfit_category
DISPLAY "Top: " + top
DISPLAY "Bottom: " + bottom
DISPLAY "Shoes: " + shoes
DISPLAY "Notes: " + notes
DISPLAY "Budget Tip: " + budget_tip
DISPLAY "--------------------------------"

END PROGRAM

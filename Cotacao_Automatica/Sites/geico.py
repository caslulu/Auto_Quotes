
# pagina do zipcode
page.goto("https://www.geico.com/auto-insurance/")
page.get_by_label("Enter your ZIP code").click()
page.get_by_label("Enter your ZIP code").fill("02149")
page.get_by_role("button", name="Review Your Quote").click()


page.goto("https://sales.geico.com/quote")
#pagina nascimento
page.get_by_placeholder("MM/DD/YYYY").fill("06/08/2004")
page.get_by_role("button", name="Next").click()

#pagina nome
page.get_by_label("First Name").fill("David ")
page.get_by_label("Last Name").click()
page.get_by_label("Last Name").fill("Silva")
page.get_by_role("button", name="Next").click()

#pagina endereco
page.get_by_placeholder("Enter a location").fill("33 sammertt st Everett")
page.get_by_role("button", name="Next").click()
page.get_by_text("Original 33 SAMMERTT ST").click()
page.get_by_role("button", name="Next").click()
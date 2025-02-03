for veiculo in self.lista_vin:
    page.get_by_role("link", name="Enter vehicle by VIN").click()
    page.get_by_label("Vehicle Identification Number").fill(veiculo)
    page.get_by_label("Vehicle use", exact=True).select_option("1")
    if self.financiado == "Financiado":
        page.get_by_label("Own or lease?").select_option("2")
    else:
        page.get_by_label("Own or lease?").select_option("3")
    if self.tempo_com_veiculo == "Menos de 1 ano":
        page.get_by_label("How long have you had this").select_option("E")
    elif self.tempo_com_veiculo == "1-3 anos":
        self.page.get_by_label("How long have you had this").select_option("B")
    else:
        self.page.get_by_label("How long have you had this").select_option("D")

    page.get_by_label("Learn more aboutAnnual").select_option("0 - 3,999")
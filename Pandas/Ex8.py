stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0, 'BBT': 25.5, 'F51': 19.2}
quotations = pd.Series(data=stocks)
quotations = pd.DataFrame(quotations).reset_index()
quotations.columns=['ticker', 'price']
print(quotations)

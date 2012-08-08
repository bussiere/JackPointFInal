from django import forms



class AddPlaceForm(forms.Form):
    Nom = forms.CharField(label='Nom')
    GPS = forms.CharField(label='GPS')
    Geohash = forms.CharField(label='Hash')
    Adresse1 = forms.CharField(label='AD1')
    Adresse2 = forms.CharField(label='AD2')
    Adresse3 = forms.CharField(label='AD3')
    Adresse4 = forms.CharField(label='AD4')
    CP = forms.CharField(label='CP')
    Ville = forms.CharField(label='Ville')
    Region = forms.CharField(label='Region')
    Pays = forms.CharField(label='Pays')
    Telephone = forms.CharField(label='Tel')
    URL1 = forms.CharField(label='URL1')
    URL2 = forms.CharField(label='URL2')
    URL3 = forms.CharField(label='URL3')
    URL4 = forms.CharField(label='URL4')
    URL5 = forms.CharField(label='URL5')
    Transport1 = forms.CharField(label='Transport1')
    Transport2 = forms.CharField(label='Transport2')
    Transport3 = forms.CharField(label='Transport3')
    Transport4 = forms.CharField(label='Transport4')
    Transport5 = forms.CharField(label='Transport5')
    Transport6 = forms.CharField(label='Transport6')
    Commentaire = forms.CharField(label='Commentaire',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
  
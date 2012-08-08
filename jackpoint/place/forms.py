from django import forms



class AddPlaceForm(forms.Form):
    Nom = forms.CharField(label='Nom')
    GPS = forms.CharField(label='GPS')
    Geohash = forms.CharField(label='hash')
    Adresse1 = forms.CharField(label='AD1')
    Adresse2 = forms.CharField(label='AD2')
    Adresse3 = forms.CharField(label='AD3')
    Adresse4 = forms.CharField(label='AD4')
    Reponse = forms.CharField(label='Commentaire',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
  
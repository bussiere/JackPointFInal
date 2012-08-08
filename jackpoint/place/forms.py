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
    LundiM1 = forms.CharField(label='LundiM1')
    LundiM2 = forms.CharField(label='LundiM2')
    LundiAM1 = forms.CharField(label='LundiAM1')
    LundiAM2 = forms.CharField(label='LundiAM2')
    MardiM1 = forms.CharField(label='MardiM1')
    MardiM2 = forms.CharField(label='MardiM2')
    MardiAM1 = forms.CharField(label='MardiAM1')
    MardiAM2 = forms.CharField(label='MardiAM2')
    MercrediM1 = forms.CharField(label='MercrediM1')
    MercrediM2 = forms.CharField(label='MercrediM2')
    MercrediAM1 = forms.CharField(label='MercrediAM1')
    MercrediAM2 = forms.CharField(label='MercrediAM2')
    JeudiM1 = forms.CharField(label='JeudiM1')
    JeudiM2 = forms.CharField(label='JeudiM2')
    JeudiAM1 = forms.CharField(label='JeudiAM1')
    JeudiAM2 = forms.CharField(label='JeudiAM2')
    VendrediM1 = forms.CharField(label='VendrediM1')
    VendrediM2 = forms.CharField(label='VendrediM2')
    VendrediAM1 = forms.CharField(label='VendrediAM1')
    VendrediAM2 = forms.CharField(label='VendrediAM2')
    SamediM1 = forms.CharField(label='SamediM1')
    SamediM2 = forms.CharField(label='SamediM2')
    SamediAM1 = forms.CharField(label='SamediAM1')
    SamediAM2 = forms.CharField(label='SamediAM2')
    DimancheM1 = forms.CharField(label='DimancheM1')
    DimancheM2 = forms.CharField(label='DimancheM2')
    DimancheAM1 = forms.CharField(label='DimancheAM1')
    DimancheAM2 = forms.CharField(label='DimancheAM2')
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
  
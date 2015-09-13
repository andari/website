class LicenceForm(ModelForm):
    class Meta:
        model = licence     

LicenceFormset = inlineformset_factory(licence, 
    fields=('licence_number', 'scan_time'), extra=1, 
    can_delete=False) 
from django import forms

class VentaForm(forms.Form):
    local_id = forms.IntegerField(label = "Local ID", widget=forms.NumberInput(attrs={'class': 'form-control w-auto'}))
    venta_fecha = forms.DateField(label = "Fecha de Venta ", widget=forms.TextInput(attrs={'class': 'form-control w-auto', 'type':'date'}))
    venta_monto = forms.IntegerField(label = "Monto", widget=forms.NumberInput(attrs={'class': 'form-control w-auto'}))
    venta_cantidad = forms.IntegerField(label = "Cantidad", widget=forms.NumberInput(attrs={'class': 'form-control w-auto'}))
                                        
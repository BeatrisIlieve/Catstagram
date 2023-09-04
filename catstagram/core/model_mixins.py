class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ';'.join(f'{key}={value}' for key, value in fields)


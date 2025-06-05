from django.core.management.base import BaseCommand
from pams.models import Patient

class Command(BaseCommand):
    help = 'Seed database with dummy patients'

    def handle(self, *args, **kwargs):
        patients = [
            {"full_name": "John Doe", "age": 45, "gender": "M", "insurance_provider": "ABC Health", "policy_number": "POL123"},
            {"full_name": "Jane Smith", "age": 30, "gender": "F", "insurance_provider": "XYZ Care", "policy_number": "POL456"},
            {"full_name": "Bob Lee", "age": 29, "gender": "M", "insurance_provider": "CarePlus", "policy_number": "POL789"},
            {"full_name": "Alice Brown", "age": 35, "gender": "F", "insurance_provider": "MediSafe", "policy_number": "POL321"},
            {"full_name": "Charlie White", "age": 50, "gender": "O", "insurance_provider": "SecureLife", "policy_number": "POL654"},
        ]
        for p in patients:
            Patient.objects.create(**p)
        self.stdout.write(self.style.SUCCESS('5 patients added!'))

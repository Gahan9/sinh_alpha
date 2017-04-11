from django.dispatch import Signal

state_audit_signal = Signal(providing_args=["user", "old_state", "new_state"])
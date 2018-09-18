from enigma.machine import EnigmaMachine

ciphertext = 'ERMJLADMAEOILPIDHPCNYJGJC'

machine = EnigmaMachine.from_key_sheet(
    rotors='VIII VI VIII',
    reflector='C',
    ring_settings=[19,7,16],
    plugboard_settings='QW AS ER DF TZ GH UI JK OP LY')
machine.set_display('HAX')
msg_key = machine.process_text('HAX')
machine.set_display(msg_key)
plaintext = machine.process_text(ciphertext)
print(plaintext)
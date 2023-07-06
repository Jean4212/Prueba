import bcrypt

def hash_password(password):
    # Generar un salt aleatorio con un factor de trabajo (work factor) de 12
    salt = bcrypt.gensalt(12)

    # Generar el hash de la contraseña utilizando el salt y el factor de trabajo
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Retornar el hash de la contraseña como una cadena de texto
    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    # Verificar si la contraseña coincide con el hash almacenado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Ejemplo de uso
password = "1234"

# Hashear la contraseña
hashed_password = hash_password(password)

print(hashed_password)

# Verificar la contraseña
is_password_correct = verify_password(password, hashed_password)

print("Contraseña correcta:", is_password_correct)
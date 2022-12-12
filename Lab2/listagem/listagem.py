from Lab2.banco import conn


def listar_cartao():
	cursor= conn.cursor()
	sent = f"SELECT * FROM thayane_bitencourt.cartao"
	cursor.execute(sent)
	now = cursor.fetchall()
	return now


def listar_onibus():
	cursor= conn.cursor()
	sent = f"SELECT * FROM thayane_bitencourt.onibus"
	cursor.execute(sent)
	now = cursor.fetchall()
	return now


def listar_motorista():
	cursor= conn.cursor()
	sent = f"SELECT * FROM thayane_bitencourt.motorista"
	cursor.execute(sent)
	now = cursor.fetchall()
	return now


def listar_usuario():
	cursor= conn.cursor()
	sent = f"SELECT * FROM thayane_bitencourt.usuario"
	cursor.execute(sent)
	now = cursor.fetchall()
	return now
package br.estacio;

import br.estacio.input.UsersInput;
import br.estacio.model.Users;

public class Main {
	public static void main(String[] args) {
		UsersInput input = new UsersInput();
		Users users = new Users().setEmail(input.lerEmail()).setName(input.lerNome()).setId(new Integer(input.lerID()));
		System.out.println(users);
	}

}

package br.estacio;

import br.estacio.input.UsersInput;
import br.estacio.model.Users;

public class Main {
	public static void main(String[] args) {
		UsersService service = new UsersService();
		UsersInput input = new UsersInput();

		Users users1 = new Users().setEmail(input.lerEmail()).setName(input.lerNome())
				.setId(new Integer(input.lerID()));
		service.adicionar(users1);
		Users users2 = new Users().setEmail(input.lerEmail()).setName(input.lerNome())
				.setId(new Integer(input.lerID()));
		service.adicionar(users2);
		System.out.println(users);
	}

}

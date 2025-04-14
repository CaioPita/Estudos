package br.estacio.input;

import java.util.Scanner;

public class UsersInput {
Scanner in;
	public String lerID() {
		System.out.println("Entre com id:");
		 in = new Scanner(System.in);
		return in.nextLine();
	}

	public String lerNome() {
		System.out.println("Entre com nome:");
		 in = new Scanner(System.in);
		return in.nextLine();
	}

	public String lerEmail() {
		System.out.println("Entre com Email:");
		in = new Scanner(System.in);
		return in.nextLine();
	}
}
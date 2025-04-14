package br.estacio.model;

public class Users {
	private Integer id;
	private String name;
	private String email;

	public Users(Integer id, String name, String email) {
		super();
		this.id = id;
		this.name = name;
		this.email = email;
	}

	public Users() {
		// TODO Auto-generated constructor stub
	}

	public Integer getId() {
		return id;
	}

	public Users setId(Integer id) {
		this.id = id;
		return this;
	}

	public String getName() {
		return name;
	}

	public Users setName(String name) {
		this.name = name;
		return this;
	}

	public String getEmail() {
		return email;
	}

	public Users setEmail(String email) {
		this.email = email;
		return this;
	}

}

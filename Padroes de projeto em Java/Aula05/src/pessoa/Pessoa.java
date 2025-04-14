package pessoa;

public class Pessoa {

	private String nome;
	private Endereco endereco;

	public Pessoa(String nome, Endereco endereco) {
		this.nome = nome;
		this.endereco = endereco;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}

	public Pessoa cloneShallow() {
		return new Pessoa(nome, endereco);
	}

	public Pessoa cloneDeep() {
		return new Pessoa(nome, new Endereco(endereco.getRua()));
	}

	@Override
	public String toString() {
		return "Pessoa [nome=" + nome + "]";
	}

}

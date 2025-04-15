package trabalho;

public class Documento {
	private String titulo;
	private String conteudo;
	private Formato formato;

	public Documento(String titulo, String conteudo, Formato formato) {
		this.titulo = titulo;
		this.conteudo = conteudo;
		this.formato = formato;
	}

	// Cópia rasa (shallow): compartilha o mesmo objeto Formato
	public Documento cloneShallow() {
		return new Documento(titulo, conteudo, formato);
	}

	// Cópia profunda (deep): cria novo objeto Formato
	public Documento cloneDeep() {
		return new Documento(titulo, conteudo, new Formato(formato.getTipo()));
	}

	// Getters e Setters para testar
	public Formato getFormato() {
		return formato;
	}
}

package Manager;

import pessoa.Endereco;
import pessoa.Pessoa;

public class Documento {
	private String titulo;
	private String conteudo;
	private String formato;
	
	public Documento(String titulo, String conteudo, String formato) {
		this.titulo = titulo;
		this.conteudo = conteudo;
		this.formato = formato;
	}
	
	public Documento clone() {
		return new Documento(this.titulo, this.conteudo,this.formato);
	}
	
	

}

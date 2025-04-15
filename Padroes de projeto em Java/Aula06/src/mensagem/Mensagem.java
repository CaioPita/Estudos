package mensagem;

abstract class Mensagem{
	protected CanalEnvio canal;
	private String conteudo;
	
	public Mensagem(CanalEnvio canal, String conteudo) {
		this.canal = canal;
		this.conteudo = conteudo;
	}
	public void enviar() {
		canal.enviar(this);
	}
	public String getConteudo() {
		return conteudo();
	}
	private String conteudo() {
		// TODO Auto-generated method stub
		return null;
	}
	
	

}

package trabalho;

public class ConfigManager {
	
	private ConfigManager instancia;
	private String configuracao;
	private Documento prototipoDocumento;
	
	public ConfigManager getInstancia() {
		return instancia;
	}
	
	public String getConfiguracao() {
		return configuracao;
	}
	public void setConfiguracao(String configuracao) {
		this.configuracao = configuracao;
	}
	public Documento getPrototipoDocumento() {
		return prototipoDocumento;
	}
	public void setPrototipoDocumento(Documento prototipoDocumento) {
		this.prototipoDocumento = prototipoDocumento;
	}
	
	
}


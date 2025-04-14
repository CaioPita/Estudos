package padrao_prototype;

public class Main {
	
	public static void main(String[] args) {
		// Obtém uma configuração de Desenvolvimento(Clone do protótipo)
		AmbienteConfig devClone = AmbientePrototypeRegistry.getPrototipo("DEV");
		devClone.exibirInfo();
		// Podemos customizar esse clone,se necessário
		devClone.setUrl("http//dev.featureX.local");
		devClone.setUsuario("devFeatureUser");
		devClone.setTimeoutSegundos(45);
		devClone.exibirInfo();
		// Obtém uma configuração de Produção(Clone de protótipo)
		AmbienteConfig prodClone = AmbientePrototypeRegistry.getPrototipo("PROD");
		prodClone.exibirInfo();
		// Personaliza se necessário
		prodClone.setUrl("https://prod-novo.suaempresa.com");
		prodClone.setSenha("senhaNova123");
		prodClone.exibirInfo();
	}

}

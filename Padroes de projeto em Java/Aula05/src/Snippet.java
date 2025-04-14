

public class Snippet {
	public void exibirInfo() {
			System.out.println("Ambiente de Produção: ");
			System.out.println("URL:" + getUrl());
			System.out.println("Usuário: " + getUsuario());
			System.out.println("Timeout: " + getTimeoutSegundos()+ "s");
			System.out.println("Log Detalhado: " + isLogDetalhado());
			System.out.println("--------------------------------");
		}
}
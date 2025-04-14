package padrao_builder;
// Builder contreto 
public class XlsNotaNegociacaoBuilder implements NotaNegociacaoBuilder {
	private NotaNegociacao nota;
	public XlsNotaNegociacaoBuilder() {
		this.nota = new NotaNegociacao();
	}
	@Override
	public void buildCabecalho() {
		nota.adicionarConteudo("XLS: Cabeçalho da Nota");
	}
	@Override
	public void buildOperacoes() {
		nota.adicionarConteudo("XLS: Lista de operações");
	}
	@Override
	public void buildSumario() {
		nota.adicionarConteudo("XLS: Sumario com totais e taxas");
	}
	@Override
	public NotaNegociacao getNota() {
		return nota;
	}
}

package padrao_builder;
//Interface do Builder que define os passos de construção
public interface NotaNegociacaoBuilder {
	void buildCabecalho();
	void buildOperacoes();
	void buildSumario();
	NotaNegociacao getNota();

}

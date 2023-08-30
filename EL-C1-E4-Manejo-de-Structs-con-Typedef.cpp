#include <stdio.h>
#include <stdlib.h>

typedef struct{
	char marca[50];
	int modelo;
	char placa[50];
	
} Carro;

typedef struct{
	int nit;
	char nombre[10];
	Carro vcarro[2];
}Concesionario;

void llenarDatos(Concesionario *cons);
void imprimirDatos(Concesionario cons);

int main(){
	
	Concesionario cons;
//	Carro vcar[2];
	
//	strcpy(car.placa, "MJT 410");
//	strcpy(car.marca, "KIA");
//	car.modelo = 2020;

	llenarDatos(&cons);
	imprimirDatos(cons);

	return 0;
}

void llenarDatos(Concesionario *cons){
	printf("Ingrese el NIT: ");
	scanf("%d", &(cons->nit));
	fflush(stdin);
	printf("Ingrese el nombre: ");
	gets(cons->nombre);
	for(int i = 0; i < 2; i++){
		fflush(stdin);
		printf("\nIngrese los datos del carro #%d \n", i+1);
		printf("Ingrese la placa: ");
		gets(cons->vcarro[i].placa);		
		printf("Ingrese la marca: ");
		gets(cons->vcarro[i].marca);
		printf("Ingrese el modelo: ");
		scanf("%d", &cons->vcarro[i].modelo);		
	}
}
void imprimirDatos(Concesionario cons){
	printf("\nDatos del Concesionario\n");
	printf("NIT: %d \n", cons.nit);
	printf("Nombre: %s \n", cons.nombre);
	for(int i = 0; i < 2; i++){
		printf("Datos carro No %d", i + 1);
		printf("La placa es: %s\n", cons.vcarro[i].placa);
		printf("La marca es: %s\n", cons.vcarro[i].marca);
		printf("El modelo es: %d\n", cons.vcarro[i].modelo);		
	}
}
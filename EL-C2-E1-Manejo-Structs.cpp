#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Carro
{
	char placa[50];
	char marca[50];
	int modelo;
//}car = {"MJT 410","KIA",2020};
};

void llenarDatos(struct Carro *car);

int main()
{
	Carro car;
//	strcpy(car.placa, "MJT 410");
//	strcpy(car.marca, "KIA");
//	car.modelo = 2020;
	
	llenarDatos(&car);
	printf("La placa es: %s\n", car.placa);
	printf("La marca es: %s\n", car.marca);
	printf("El modelo es: %d\n", car.modelo);
	
	return 0;
}

void llenarDatos(struct Carro *car){
	printf("Ingrese la placa: ");
	gets(car->placa);
	printf("Ingrese la marca: ");
	gets(car->marca);
	printf("Ingrese el modelo: ");
	scanf("%d", &(car->modelo));
}
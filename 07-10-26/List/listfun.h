//Functions created by G V V Sharma (Cleaned for core execution)

//Function declaration
double Listdet(avyuh *a);//determinant of a 2x2 matrix
double Listrace(avyuh *c);//matrix trace
double Listnorm(avyuh *a);//norm of a vector
double Listdot(avyuh *a, avyuh * b);//inner product
double ListVecdot(sadish *a, sadish * b);//inner product
avyuh *Listsub(avyuh *a, avyuh *b);//subtract two matrices
avyuh *Listadd(avyuh *a, avyuh *b);//add two matrices
sadish *ListVecadd(sadish *a, sadish *b);//add two matrices
sadish *ListVecsub(sadish *a, sadish *b);//subtract two vectors
avyuh *Listscale(avyuh *a, double k);//scale matrix
sadish *Listvecscale(sadish *a, double k);//scale vector
avyuh *Listinv(avyuh *mat, int m);//invert an m x m matrix, m <=3
avyuh *Listmul(avyuh *a, avyuh *b);//multiply matrices a and b
avyuh *Listsec(avyuh *a, avyuh * b,double k);//section formula
sadish *ListVecSec(sadish *a, sadish *b, double k);
//End function declaration

//add two matrices
avyuh *Listadd(avyuh *a, avyuh *b){
	avyuh *c= (avyuh *)malloc(sizeof(avyuh)), *tempb = b, *head; 
	c->next = NULL;
	head = c;
	 for(avyuh *tempa=a;tempa!=NULL;tempa=tempa->next){
                c->vector = ListVecadd(tempa->vector,tempb->vector);
                tempb = tempb->next;
	if(tempa->next!=NULL){
		c->next = (avyuh *)malloc(sizeof(avyuh));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//Sum of vectors
sadish *ListVecadd(sadish *a, sadish *b){
	sadish *head = (sadish *)malloc(sizeof(sadish)), *c, *tempb=b;
	c = head; 
	head->next = NULL;
	for(sadish *tempa=a;tempa!=NULL;tempa=tempa->next){
                c->data = tempa->data+tempb->data;
                tempb = tempb->next;
	if(tempa->next!=NULL){
		c->next = (sadish *)malloc(sizeof(sadish));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//inner product
double ListVecdot(sadish *a, sadish *b){
	double val = 0;
	sadish *tempa=a, *tempb=b;
	while(tempa !=NULL){
		val += tempa->data*tempb->data;
		tempa = tempa->next;
		tempb = tempb->next;
	}
	return val;
}

double Listdot(avyuh *a, avyuh *b){
	return ListVecdot(a->vector, b->vector);
}

sadish *ListVecsub(sadish *a, sadish *b){
	sadish *head = (sadish *)malloc(sizeof(sadish)), *c, *tempb=b;
	c = head; 
	head->next = NULL;
	for(sadish *tempa=a;tempa!=NULL;tempa=tempa->next){
		c->data = tempa->data-tempb->data;
		tempb = tempb->next;
	if(tempa->next!=NULL){
		c->next = (sadish *)malloc(sizeof(sadish));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//subtract two matrices
avyuh *Listsub(avyuh *a, avyuh *b){
	avyuh *c= (avyuh *)malloc(sizeof(avyuh)),  *tempb = b, *head; 
	c->next = NULL;
	head = c;
	for(avyuh *tempa=a;tempa!=NULL;tempa=tempa->next){
		c->vector = ListVecsub(tempa->vector,tempb->vector);
		tempb = tempb->next;
	if(tempa->next!=NULL){
		c->next = (avyuh *)malloc(sizeof(avyuh));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//norm of a vector
double Listnorm(avyuh *a){
	return sqrt(Listdot(a,a));
}

//Matrix multiplication
avyuh *Listmul(avyuh *a, avyuh *b){
	avyuh *c=(avyuh *)malloc(sizeof(avyuh)),*atemp, *btemp;
	avyuh *head = c;
	sadish *cvec=(sadish *)malloc(sizeof(sadish));
	head->next = NULL;
	for(atemp=a; atemp !=NULL; atemp=atemp->next){
		cvec=(sadish *)malloc(sizeof(sadish));
		cvec->next = NULL;
		c->vector = cvec;  
		for(btemp=b; btemp !=NULL; btemp=btemp->next){
			cvec->data=ListVecdot(atemp->vector, btemp->vector);
		if(btemp->next!=NULL){
			cvec->next = (sadish *)malloc(sizeof(sadish));
			cvec->next->next=NULL;
			cvec= cvec->next;
		}
		}

		if(atemp->next!=NULL){
			c->next = (avyuh *)malloc(sizeof(avyuh));
			c->next->next=NULL;
			c= c->next;
		}
	}
	return head;
}

//scale vector
sadish *Listvecscale(sadish *a, double k){
	sadish *head = (sadish *)malloc(sizeof(sadish)), *c;
	c = head; 
	head->next = NULL;
	for(sadish *tempa=a;tempa!=NULL;tempa=tempa->next){
		c->data = k*tempa->data;
	if(tempa->next!=NULL){
		c->next = (sadish *)malloc(sizeof(sadish));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//scale matrix
avyuh *Listscale(avyuh *a, double k){
	avyuh *head = (avyuh *)malloc(sizeof(avyuh)), *c;
	c = head; 
	head->next = NULL;
	for(avyuh *tempa=a;tempa!=NULL;tempa=tempa->next){
		c->vector = Listvecscale(tempa->vector, k);
	if(tempa->next!=NULL){
		c->next = (avyuh *)malloc(sizeof(avyuh));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//section formula for vectors
sadish *ListVecSec(sadish *a, sadish *b,double k){
	sadish *head=(sadish *)malloc(sizeof(sadish));
	head->next = NULL;
	for(sadish *c = head;a!=NULL;a=a->next){
		c->data= (k*b->data+a->data)/(k+1);
		b=b->next;
	if(a->next!=NULL){
		c->next = (sadish *)malloc(sizeof(sadish));
		c->next->next=NULL;
		c= c->next;
	}
	}
	return head;
}

//section formula for matrices
avyuh *Listsec(avyuh *a, avyuh *b, double k){
	avyuh *c= (avyuh *)malloc(sizeof(avyuh)), *tempb = b, *head; 
	c->next = NULL;
	head = c;
	 for(avyuh *tempa=a;tempa!=NULL;tempa=tempa->next){
                c->vector = ListVecSec(tempa->vector,tempb->vector, k);
                tempb = tempb->next;
	if(tempa->next!=NULL){
		c->next = (avyuh *)malloc(sizeof(avyuh));
		c->next->next=NULL;
		c= c->next;
	}
	}
	 return head;
}

//matrix trace
double Listrace(avyuh *c){
	double temp=0;
	sadish *vec;
	for(int i=0;c!=NULL;c=c->next,i++){
		vec = c->vector;
		for(int k = 0; k < i; k++){
			vec = vec->next;
		}
		temp +=vec->data;
	}
	return temp;
}

//determinant of a 2x2 matrix
double Listdet(avyuh *a){
	double temp1, temp2;	
	temp1 = a->vector->data;
	temp2 = a->vector->next->data;
	a = a->next;
	temp2 = a->vector->data*temp2;
	temp1 = a->vector->next->data*temp1;
	return temp1-temp2;
}

avyuh *Listinv(avyuh *mat, int m){
    return mat; 
}


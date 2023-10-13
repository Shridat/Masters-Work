#include<iostream>
#include<omp.h>

int main(){
    int size = 64;
    int array[size];
    #pragma omp parallel num_threads(16)
    {
        #pragma omp for
            for(int i=0; i<size; i++){
                array[i] = 1;
            }
        #pragma omp for
            for(int i=0; i<size; i++){
                array[i]+=2*i;
            }
    }
    std::cout<<"Initialized array after multiplying and adding by 2*i";
    for(int i=0; i<size; i++){
        std::cout<<array[i]<<" ";
    }
    std::cout<<std::endl;
    int local_count,count = 0;
    #pragma omp parallel private(local_count) shared(count) num_threads(16)
    {
        int local_count = 0;
        int thread_id = omp_get_thread_num();
        #pragma omp for schedule(static,1)
        for(int i=0; i<size; i++){
            if(array[i]%3==0){
                local_count+=1;
            }
        }
        #pragma omp critical
        count+=local_count;
    }
    std::cout<<"Total values divisible by 3 = "<<count;
    return 0;
}
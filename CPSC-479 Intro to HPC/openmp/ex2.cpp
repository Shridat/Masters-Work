#include <iostream>
#include <omp.h>

int main() {
    const int N = 100;
    int a[N];
    int nx=0;
    // Initialize
    for (int i = 0; i < N; i++) {
        a[i] = i;
    }

    // Compute sum
    int local_sum, sum = 0;

#pragma omp parallel private(local_sum) shared(sum)
    {
        local_sum = 0;
        nx = omp_get_num_threads();
        // The array is distributed statically between threads
#pragma omp for schedule(static, 1)
        for (int i = 0; i < N; i++) {
            local_sum += a[i];
        }

        // Each thread calculates its local_sum.
        // All threads have to add to the global sum.
#pragma omp critical
        sum += local_sum;
    }

    std::cout << "sum=" << sum << " should be " << N * (N - 1) / 2 << std::endl;
    return 0;
}

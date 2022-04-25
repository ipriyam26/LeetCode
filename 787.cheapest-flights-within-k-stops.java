import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    class Flight   {
        int id;
        int price;
        int stop;

        Flight(int id, int price, int stop) {
            this.id = id;
            this.price = price;
            this.stop = stop;
        }

    }

    public int[][] adjMatrix(int[][] arr, int n) {
        int[][] adjMatrix = new int[n][n];
        for (int i = 0; i < arr.length; i++) {
            adjMatrix[arr[i][0]][arr[i][1]] = arr[i][2];
        }
        return adjMatrix;
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        PriorityQueue<Flight> pq = new PriorityQueue<>((n1,n2)->n1.price-n2.price);
        int[][] adj = adjMatrix(flights, n);
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(src, 0);
        pq.add(new Flight(src, 0, k + 1));

        while (!pq.isEmpty()) {
            Flight flight = pq.poll();
            // int curr = flight.id;
            // int price = flight.price;
            // int stop = flight.stop;
            if (flight.id == dst)
                return flight.price;

            for (int i = 0; i < n; i++) {
                if (adj[flight.id][i] != 0) {
                    int newPrice = flight.price + adj[flight.id][i];
                    if (!map.containsKey(i) || map.get(i) > newPrice) {
                        map.put(i, newPrice);
                        if (flight.stop < k) {
                            pq.add(new Flight(i, newPrice, flight.stop - 1));
                        }
                    }
                }
            }

        }
        return map.get(dst);
 

    }
}
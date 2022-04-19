import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/*
 * @lc app=leetcode id=399 lang=java
 *
 * [399] Evaluate Division
 */

// @lc code=start
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = buildGraph(equations, values);
        double[] results = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            results[i] = getPathWeight(queries.get(i).get(0), queries.get(i).get(1), new HashSet<>(), graph);
        }
        return results;
        
    }

    public double getPathWeight(String start,String end,Set<String> visited,Map<String,Map<String,Double>> graph){
        
        if(!graph.containsKey(start)){
            return -1.0;
        }

        if(graph.get(start).containsKey(end)){
            return graph.get(start).get(end);
        }

        visited.add(start);

        for (Map.Entry<String,Double> rEntry : graph.get(start).entrySet()) {
            if(!visited.contains(rEntry.getKey())){
                double pathWeight = getPathWeight(rEntry.getKey(), end, visited, graph); 
                if(pathWeight!=-1.0){
                    return rEntry.getValue()*pathWeight;
                }
            }


        }
        return -1.0;
    }

    public Map<String, Map<String, Double>> buildGraph(List<List<String>> equations, double[] values) {

        Map<String, Map<String, Double>> graph = new HashMap<>();
        String first, second;
        for (int i = 0; i < equations.size(); i++) {
            first = equations.get(i).get(0);
            second = equations.get(i).get(1);
            graph.putIfAbsent(first, new HashMap<>());
            graph.get(first).put(second, values[i]);
            graph.putIfAbsent(second, new HashMap<>());
            graph.get(second).put(first, 1 / values[i]);

        }

        return graph;

    }
}
// @lc code=end

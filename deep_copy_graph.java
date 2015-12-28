/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        //deep copy
        if (node==null) return null;
        
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        UndirectedGraphNode head = new UndirectedGraphNode(node.label);
        map.put(node, head);
        DFS(map, node);
        return head;
    }
    
    private void DFS(HashMap<UndirectedGraphNode, UndirectedGraphNode> map, UndirectedGraphNode node){
        if (node==null) return;
        
        for (UndirectedGraphNode nb: node.neighbors){
            // if not there, add neighbours, and DFS
            if (!map.containsKey(nb)){
                UndirectedGraphNode n = new UndirectedGraphNode(nb.label);
                map.put(nb, n);
                DFS(map, nb);
            }
            //
            map.get(node).neighbors.add(map.get(nb));
        }
    }
}

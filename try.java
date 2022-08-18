class UnionFind{
int[] size;
int[] id;

    public UnionFind(int size){
        this.size = size;
        this.id = new int[size];
        this.size = new int[size];
        for(int i = 0; i < size; i++){
            this.id[i] = i;
            this.size[i] = 1;
        }
    }

    public  int find(int x){

        int root = x;
        while(root != id[root]){
            root = id[root];
        }
        //compress path
        while(x != root){
            int temp = id[x];
            id[x] = root;
            x = temp;
        }
        return root;

    }
    public void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if(rootX == rootY){
            return;
        }
        if(size[rootX] > size[rootY]){
            id[rootY] = rootX;
            size[rootX] += size[rootY];
        }else{
            id[rootX] = rootY;
            size[rootY] += size[rootX];
        }
    }
    public int findLargestComponent(){
        int max = 0;
        for(int i = 0; i < size.length; i++){
            max = Math.max(max, size[i]);
        }
        return max;
    }


}
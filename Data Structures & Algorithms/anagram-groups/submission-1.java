class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<HashMap<Character, Integer>> hashmaps = new ArrayList<>();
        List<List<String>> groups = new ArrayList<>();

        for (String str : strs) {
            //Calcular mapa per a la paraula str
            HashMap<Character, Integer> strMap = new HashMap<>();
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                int n = strMap.getOrDefault(c, 0);
                strMap.put(c, n+1);
            }
            //Comprovar si el mapa coincideix amb algun de la llista
            boolean found = false;
            for (int i = 0; i < hashmaps.size(); i++) {
                if (strMap.equals(hashmaps.get(i))) {
                    //Si coincideix, afegir-lo a la llista corresponent
                    groups.get(i).add(str);
                    found = true;
                    break;
                }
            }
            //Si no coincideix, afegir-lo en les 2 llistes
            if (!found) {
                hashmaps.add(strMap);
                List<String> newGroup = new ArrayList<>();
                newGroup.add(str);
                groups.add(newGroup);
            }
        }
        return groups;
    }
}

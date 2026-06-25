class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, Integer> hashmap = new HashMap<>();
        List<List<String>> groups = new ArrayList<>();
        int currentIndex = 0;
        for (String str : strs) {
            //Plenar array de lletres
            int[] letters = new int[26];
            for (int i = 0; i < str.length(); i++) {
                letters[str.charAt(i) - 'a'] += 1;
            }
            //Buscar coincidència en el hashmap
            Integer index = hashmap.get(Arrays.toString(letters));
            if (index == null) { //Si no existeix es crea el grup
                hashmap.put(Arrays.toString(letters), currentIndex);
                currentIndex++;
                List<String> newGroup = new ArrayList<String>();
                newGroup.add(str);
                groups.add(newGroup);
            } else { //Si existeix l'afegeix al seu grup
                groups.get(index).add(str);
            }
        }
        return groups;
    }
}

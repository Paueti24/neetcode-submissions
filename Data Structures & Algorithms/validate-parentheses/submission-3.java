class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        
        // 1. Optimización de descarte: si es impar, es imposible que sea válido
        if (len % 2 != 0) return false;
        
        // Reducimos el tamaño de la pila. Como máximo necesitaremos len / 2 
        // espacios, ya que si hay más aperturas que la mitad, nunca se cerrarán.
        char[] stack = new char[len / 2];
        int head = 0;
        
        // 2. Usamos bucle indexado para evitar la asignación de memoria de toCharArray()
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            
            // 3. El switch genera una "Jump Table" (tableswitch) ultra rápida en Bytecode
            switch (c) {
                case '(':
                    if (head >= stack.length) return false; // Evita desbordamiento si hay demasiadas aperturas
                    stack[head++] = ')';
                    break;
                case '{':
                    if (head >= stack.length) return false;
                    stack[head++] = '}';
                    break;
                case '[':
                    if (head >= stack.length) return false;
                    stack[head++] = ']';
                    break;
                default:
                    // Si es un carácter de cierre, validamos la pila
                    if (head == 0 || stack[--head] != c) {
                        return false;
                    }
                    break;
            }
        }
        
        return head == 0;
    }
}
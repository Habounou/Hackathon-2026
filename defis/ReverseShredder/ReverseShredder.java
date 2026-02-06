import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class ReverseShredder {

    private static boolean checkAllSubstrings(String bigString, List<String> smallStrings) {
        for (String sub : smallStrings) {
            if (sub == null) continue;
            if (bigString.indexOf(sub) < 0) return false;
        }
        return true;
    }

    private static void verify(String bigString, List<String> smallStrings) {
        if (bigString == null) {
            System.out.println("No string...");
            return;
        }
        if (checkAllSubstrings(bigString, smallStrings)) {
            System.out.println("All substrings were found!");
            System.out.println("Length : " + bigString.length());
        } else {
            System.out.println("One or more substrings are missing.");
        }
    }

    private static List<String> readFrags(String filename) throws IOException {
        List<String> frags = new ArrayList<>();
        for (String line : Files.readAllLines(Paths.get(filename), StandardCharsets.UTF_8)) {
            String cleaned = line;
            if (cleaned == null) continue;
            if (cleaned.isEmpty()) continue;
            frags.add(cleaned);
        }
        return frags;
    }

    private static List<String> initialize() throws IOException {
        // input_demo input_level_1 input_level_2 input_level_3 input_level_4
        return readFrags("input_demo.txt");
    }

    private static String reverseShreddify(List<String> frags) {
        
        // *** recommandation : écrire votre code ici ***

        return null;
    }

    public static void main(String[] args) throws IOException {
        List<String> frags = initialize();

        StringBuilder sb = new StringBuilder();
        for (String f : frags) sb.append(f);
        String solutionNaive = sb.toString();

        System.out.println(solutionNaive);
        verify(solutionNaive, frags);

        String goodSolution = reverseShreddify(frags);

        // Pour input_demo.txt la meilleure réponse (la plus courte string) est de longeur 53
        // good_solution = "Demain,_dès_l’aube,_à_l’heure_où_blanchit_la_campagne"

        System.out.println(goodSolution);
        verify(goodSolution, frags);
    }
}

import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FileReader {



    public FileReader() {
        String fileName = "data/transactions.csv";
        String line;
        String delimiter = ",";
        List<List<String>> lines = new ArrayList<>();
        try (BufferedReader br =
                     new BufferedReader(new FileReader(fileName))) {
            while((line = br.readLine()) != null){
                List<String> values = Arrays.asList(line.split(delimiter));
                lines.add(values);
            }
            lines.forEach(System.out::println);
        } catch (Exception e){
            System.out.println(e);
        }
    }
}

